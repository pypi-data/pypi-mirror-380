"""
API for the quets project
"""
import requests                                                                                                                                                                                                   
import time, os
from datetime import datetime, timezone
from dataclasses import asdict
from dataclasses import dataclass
from dataclasses import field
from pathlib import Path


from .db import DB
from .db_sql import DBsql


__all__ = [
    "Quote",
    "QuoteDB",
    "QuoteDBsql",
    "QuoteException",
    "MissingText",
    "InvalidQuoteId",
    "BadReqest",
]

@dataclass
class Quote:
    """model for a quote.
    """    
    text: str = None
    author: str = None
    timestep: str = None 
    id: int = field(default=None, compare=False)

    @classmethod
    def from_dict(cls, d):
        """Create a Quote from a dict.

        Args:
            d (_type_): dict with quote data.

        Returns:
            _type_: Quote instance
        """        
        return Quote(**d)
    
    def to_dict(self):
        """Return a dict representation of the Quote."""
        return asdict(self)


class QuoteException(Exception):
    pass


class MissingText(QuoteException):
    pass


class InvalidQuoteId(QuoteException):
    pass

class BadReqest(QuoteException):
    pass


class QuoteDB:
    """A class to manage a database of quotes. API for quotes.
    """    
    def __init__(self, db_path):
        """initialize the QuoteDB instance.

        Args:
            db_path (_type_): Path to the database file.
        """        
        self._db_path = db_path
        self._db = DB(db_path, "quotes", ["timestep",'text', 'author'])

    def add_quote(self, quote: Quote) -> int:
        """Add a quote, return the id of quote.

        Args:
            quote (Quote): Quote instance.

        Raises:
            MissingText: if quote.text is None.

        Returns:
            int: id of the added quote.
        """        
        if not quote.text:
            raise MissingText
        if quote.author is None:
            quote.author = ""
        id = self._db.create(quote.to_dict())
        self._db.update(id, {"id": id,
                             "timestep":datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S %Z') })
        return id
    
    def get_quote(self, quote_id: int) -> Quote:
        """Return a quote with given quote_id.

        Args:
            quote_id (int): id of the quote.

        Raises:
            InvalidQuoteId: if quote_id is not in db.

        Returns:
            Quote: Quote instance.
        """        
        db_item = self._db.read(quote_id)
        if db_item is not None:
            return Quote.from_dict(db_item)
        else:
            raise InvalidQuoteId(quote_id)

    def list_quote(self, author=None):
        """Return a list of quotes.

        Args:
            author (_type_, optional): Author name to filter quotes. Defaults to None.

        Returns:
            List(Quote)): List of Quote instances.
        """        
        all = self._db.read_all()
        if author is not None:
            return [
                Quote.from_dict(t)
                for t in all
                if (t["author"] == author)
            ]
        else:
            return [Quote.from_dict(t) for t in all]

    def count(self) -> int:
        """Return the number of quotes in db."""
        return self._db.count()

    def update_quote(self, quote_id: int, quote_mods: Quote) -> None:
        """update a quote with modifications.

        Args:
            quote_id (int): id of the quote to update.
            quote_mods (Quote): Quote instance with modifications.

        Raises:
            InvalidQuoteId: if quote_id is not in db.
        """
        try:
            self._db.update(quote_id, quote_mods.to_dict())
        except KeyError as exc:
            raise InvalidQuoteId(quote_id) from exc
        
    def start(self, url: str, pause: float):
        """get quotes from url and add them to db every 'pause' seconds.

        Args:
            url (str): _url to get quotes from if not given use "https://zenquotes.io/api/random"
            pause (float): pause between requests in seconds.
        """


        # url = "https://zenquotes.io/api/random"    
                                                                                                                                                                           
        print("For stop taking quotes press 'Ctrl + C'") 
                                                                                                                                                                                                                   
        while True:                                                                                                                                                                                                   
            try:                                                                                                                                                                                                      
                response = requests.get(url)                                                                                                                                                                          
                response.raise_for_status()  # Генерирует исключение для статуса ошибки HTTP                                                                                                                          
                data = response.json()                                                                                                                                                                                
                                                                                                                                                                                                                    
                if data:                                                                                                                                                                                              
                    quote = data[0]["q"]                                                                                                                                                                              
                    author = data[0]["a"]
                    self.add_quote(Quote(text=quote, author=author))                                                                                                                                                                             
                    print(f"Added Quote: {quote} - Author: {author}")                                                                                                                                                       
                else:                                                                                                                                                                                                 
                    print("No data received.")
                print("For stop taking quotes press 'Ctrl + C'")                                                                                                                                                                        
                time.sleep(pause)  # Пауза в 1 секунду

            except requests.exceptions.RequestException as e:                                                                                                                                                         
                print(f"Error fetching quote: {e}")                                                                                                                                                                   

            except KeyboardInterrupt:                                                                                                                                                                                     
                print("\nОстановка запроса цитат пользователем.")
                break   

    def delete_quote(self, quote_id: int) -> None:
        """Delete a quote with given quote_id.

        Args:
            quote_id (int): id of the quote to delete.

        Raises:
            InvalidQuoteId: if quote_id is not in db.
        """        
        try:
            self._db.delete(quote_id)
        except KeyError as exc:
            raise InvalidQuoteId(quote_id) from exc

    def delete_all(self) -> None:
        """Remove all quotes from db."""
        self._db.delete_all()

    def path(self):
        """Return the path to the database file."""
        return self._db_path

class QuoteDBsql:
    """A class to manage a database of quotes using MySQL. API for quotes.
    """    
    def __init__(self, user, password, host = "localhost", port = 3306,  database = "quotes_db"):
        """initialize the QuoteDBsql instance.

        Args:
            user (str): username for the database.
            password (str): password for the database.
            host (str, optional): hpstname for the database. Defaults to "localhost".
            port (int, optional): port for the database. Defaults to 3306.
            database (str, optional): database name. Defaults to "quotes_db".
        """        
        self._db = DBsql(user, password, host, port, database)

    def add_quote_sql(self, quote: Quote) -> None:
        """Add a quote to the database.

        Args:
            quote (Quote): Quote instance.

        Raises:
            MissingText: if quote.text is None.
        """ 
        if not quote.text:
            raise MissingText
        if quote.author is None:
            quote.author = ""
        self._db.create(quote.to_dict())
        
 
    def list_quote(self, author=None) -> list[Quote]:
        """Return a list of quotes.

        Args:
            author (str, optional): Author name to filter quotes. Defaults to None.

        Returns:
            list[Quote]: List of Quote instances.
        """        
        all = self._db.read_all()
        if author is not None:
            return [
                Quote.from_dict(t)
                for t in all
                if (t["author"] == author)
            ]
        else:
            return [Quote.from_dict(t) for t in all]

        
    def get_some_quotes(self, url: str):
        """Get 50 quotes from url and add them to db.

        Args:
            url (str): _url to get quotes from if not given use "https://zenquotes.io/api/quotes"
        """        

        # url = "https://zenquotes.io/api/quotes"    
                                                                                                                                                                           
        try:                                                                                                                                                                                                      
            response = requests.get(url)                                                                                                                                                                          
            response.raise_for_status()                                                                                                                      
            data = response.json()                                                                                                                                                                                
            if data:
                for item in data:                                                                                                                                                                                              
                    quote = item["q"]                                                                                                                                                                              
                    author = item["a"]
                    self.add_quote_sql(Quote(text=quote, author=author))                                                                                                                                                                            
                    print(f"Added Quote: {quote} - Author: {author}") 
                    time.sleep(0.5)   
                print('Added 50 quotes, you can see them using the "art_studio_t list_sql" command')                                                                                                                                               
            else:                                                                                                                                                                                                 
                print("No data received.")
        except requests.exceptions.RequestException as err:                                                                                                                                                         
            print(f"Error fetching quote: {err}")                                                                                                                                                                   

    def get_latest(self, number) -> list[Quote]:
        """Return the latest 'number' quotes default 5

        Args:
            number (_type_): number of quotes to return.

        Returns:
            list[Quote]: List of Quote instances.
        """        
        all = self._db.get_latest(number)
        return [Quote.from_dict(t) for t in all]

    def delete_all(self) -> None:
        """Remove all quotes from db mySQL.
        """        
        self._db.delete_all()

# todo: uncomment for testing
# if __name__ == "__main__":
#     ob = QuoteDB(Path(os.getcwd()))
#     # ob.start("https://zenquotes.io/api/random",10)
#     print(ob.list_quote())
#     print(ob.count())
#     # ob.delete_all()

#     ob.delete_quote(1)
#     ob.update_qote(2, Quote(text="New text"))
#     print(ob.get_quote(2))
#     ob.add_quote(Quote(text="Some text", author="Some author"))
#     print(ob.list_quote())  
#     print(ob.count())
#     ob.delete_all()      

