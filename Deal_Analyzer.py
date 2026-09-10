from Models import Listing, Seller, CollectionItem

class DealAnalyzer:

    def Review_Score(self, seller: Seller) -> float:

        if(seller.positive_reviews == 0):
            positive_review_percentage: str = "0%"
        
        elif(seller.negative_reviews == 0):
            positive_review_percentage: str = "100%"

        else:
            total_reviews: int = seller.negative_reviews + seller.positive_reviews
            positive_ratio : float = seller.negative_reviews / total_reviews
            positive_review_percentage : str = round((100 - (positive_ratio * 100)),2)

        return positive_review_percentage
    pass

    def Sales_History_Score(self, seller : Seller) -> float:

        sales = seller.total_sales

        if(sales >= 200):
            Final_Score : float = 10.0
        elif(sales >= 150):
            Final_Score : float = 9.5
        elif(sales >= 125):
            Final_Score : float = 9.0
        elif(sales >= 100):
            Final_Score : float = 8.5
        elif(sales >= 80):
            Final_Score : float = 8.0
        elif(sales >= 70):
            Final_Score : float = 7.5
        elif(sales >= 60):
            Final_Score : float = 7.0
        elif(sales >= 50):
            Final_Score : float = 6.5
        elif(sales >= 45):
            Final_Score : float = 6.0
        elif(sales >= 40):
            Final_Score : float = 5.5
        elif(sales >= 35):
            Final_Score : float = 5.0
        elif(sales >= 30):
            Final_Score : float = 4.5
        elif(sales > 25):
            Final_Score : float = 4.0
        elif(sales >= 20):
            Final_Score : float = 3.5
        elif(sales >= 15):
            Final_Score : float = 3.0
        elif(sales >= 13):
            Final_Score : float = 2.5
        elif(sales >= 10):
            Final_Score : float = 2.0
        elif(sales >= 7):
            Final_Score : float = 1.5
        elif(sales >= 5):
            Final_Score : float = 1.0
        elif(sales >= 3):
            Final_Score : float = 0.5
        else:
            Final_Score : float = 0

        return Final_Score
    pass

    def Account_Age_Score(self, seller : Seller) -> float:##

        Age = seller.account_age_days

        if Age is None:
            return 0
        elif Age < 30: #under 1 month
            score : float = 0
        elif Age < 60: #1-2 months
            score : float = 1.0
        elif Age < 90: #2-3 months
            score : float = 2.0
        elif Age < 120: #3-4 months
            score : float = 3.0
        elif Age < 180: #4-6 months
            score : float = 4.0
        elif Age < 365: #6 months - 1 year
            score : float = 5.0
        elif Age < 730: #1-2 years
            score : float = 6.0
        elif Age < 1095: #2-3 years
            score : float = 7.0
        elif Age < 1460: #3-4 years
            score : float = 8.0
        elif Age < 1825: #4-5 years
            score : float = 9.0
        elif Age >= 1825: #5+ years
            score : float = 10.0
        
        return score
    pass


    def Calculate_Seller_Safety(self, seller : Seller) -> float:

        Seller_Review_Score = self.Review_Score(seller)
        Seller_History_Score = self.Sales_History_Score(seller)
        Seller_Age_Score = self.Account_Age_Score(seller)

        #Weighting ----------------------------------- 1.0
        W_Seller_Review_Score = Seller_Review_Score * .50
        W_Seller_History_Score = Seller_History_Score * .30
        W_Seller_Age_Score = Seller_Age_Score * .20

        score = (W_Seller_History_Score * 10) + W_Seller_Review_Score + (W_Seller_Age_Score * 10)

        return round(score, 2)
    pass

pass


#Test
#---------------------------------------------------------------------
test = Seller(
        seller_id="123",
        seller_name="John",
        positive_reviews=98,
        negative_reviews=2,
        total_sales=75,
        account_age_days=1825
    )

analyzer = DealAnalyzer()

PRS = str(analyzer.Review_Score(test))
SHS = str(analyzer.Sales_History_Score(test))
AAS = str(analyzer.Account_Age_Score(test))
SSS = str(analyzer.Calculate_Seller_Safety(test))

print("Positive Review Score " + PRS)
print("Sales History Score " + SHS)
print("Account Age Score " + AAS)
print("Seller Safety Score " + SSS)
#-------------------------------------------------------------------------
