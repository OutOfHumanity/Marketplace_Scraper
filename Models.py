from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime

# ============================================================
# SEARCH CONFIGURATION
# ============================================================

@dataclass
class SearchConfig: #Defines a single search object when called
    keyword: str
    min_price: float
    max_price: float
    pages: int
pass


# ============================================================
# COLLECTION ITEM
# ============================================================

@dataclass
class CollectionItem:

    item_id: str
    name: str

    quantity: int = 1

    notes: str = ""
pass


# ============================================================
# SELLER
# ============================================================

@dataclass
class Seller:
    seller_id: str
    seller_name: str
    
    positive_reviews: float = 0
    negative_reviews: float = 0
    stars: float = 0
    
    current_listings: int = 0
    total_sales: int = 0
    
    account_age_days: Optional[int] = None
    
    distance_miles: Optional[float] = None
    
    blocked: bool = False
    
pass


# ============================================================
# LISTING
# ============================================================

@dataclass #creating the Listing Container dataclass
class Listing:
    listing_id: str
    title: str
    price: float
    url:str

    seller: Seller
    
    description: str = ""
    location: str = ""
    
    posted_at: Optional[datetime] = None
                                    
    image_urls: List[str] = field(default_factory=list)
    
    quantity: int = 1
    
    blocked: bool = False #Listing is unblocked by default
    saved: bool = False #Listing is unsaved by default

    def __post_init__(self): #__post_init__ makes the function happen immediatly after initializing
                             #checking if the seller is blocked to then determine if the listing should be blocked also
        if self.seller.blocked:
            self.blocked = True
    
pass
