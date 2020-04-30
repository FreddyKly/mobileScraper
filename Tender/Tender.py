from typing import Optional

class Tender:
    def __init__(self,
                 title: Optional[str] = None,
                 milage: Optional[int] = None):
        self.title = title
