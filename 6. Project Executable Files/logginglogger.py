# logging/logger.py
from elasticsearch import Elasticsearch

class Logger:
    def __init__(self):
        self.es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

    def log_event(self, message, event_type="info"):
        """Log an event to Elasticsearch."""
        doc = {
            "event": message,
            "type": event_type
        }
        res = self.es.index(index="cyber-events", document=doc)
        print(f"Logged event: {res['_id']}")

if __name__ == "__main__":
    logger = Logger()
    logger.log_event("User login attempt from IP 192.168.1.100")
