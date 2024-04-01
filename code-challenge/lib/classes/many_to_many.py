class Customer:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.reviews_list =[]

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        if isinstance(first_name, str) and 1 <= len(first_name) <= 25:
            self._first_name = first_name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        if isinstance(last_name, str) and 1 <= len(last_name) <= 25:
            self._last_name = last_name 

    def reviews(self):
        return [review for review in self.reviews_list]

    def restaurants(self):
        restaurants = set()
        for review in self.reviews_list:
            restaurants.add(review.restaurant)
        return list(restaurants)

    def num_negative_reviews(self):
        negative_count = sum(1 for review in self.reviews_list if review.rating in [1, 2])
        return negative_count

    def has_reviewed_restaurant(self, restaurant):
        for review in self.reviews_list:
            if review.restaurant == restaurant:
                return True
        return False
    
class Restaurant:
    all =[]

    def __init__(self, name):
        self.name = name
        self._reviews =[]
        Restaurant.all.append(self)
       
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def  name(self, name):
        if isinstance (name, str) and 1<=len(name):
         self._name = name


    def reviews(self):
        return self._reviews

    def customers(self):
        customers = set()
        for review in self._reviews:
            customers.add(review.customer)
        return list(customers)


    def average_star_rating(self):
        if not self._reviews:  # Check if there are no reviews
            return 0.0

        total_ratings = sum(review.rating for review in self._reviews)
        average_rating = total_ratings / len(self._reviews)
        aver =round(average_rating, 1)
        return aver

    @classmethod
    def top_two_restaurants(cls):
        restaurant_with_avg_rating = {}
        for restaurant in cls.all:
            restaurant_with_avg_rating[restaurant] = restaurant.average_star_rating()
        sorted_restaurant_with_avg_rating = dict(sorted(restaurant_with_avg_rating.items(), key=lambda item: item[1], reverse=True))
        return list(sorted_restaurant_with_avg_rating.keys())[:2] if len(Review.all) > 0 else None
        
    
class Review:

    all=[]

    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self._rating = rating
        customer.reviews_list.append(self)
        restaurant._reviews.append(self)
        Review.all.append(self)

    @property
    def rating(self):
        return self._rating
    

    @rating.setter
    def rating(self, rating):
        if isinstance(rating, int) and 1 <= rating <= 5:
            self._rating = self._rating

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, customer):
        if isinstance(customer, Customer):
            self._customer = customer

    @property
    def restaurant(self):
        return self._restaurant

    @restaurant.setter
    def restaurant(self, restaurant):
        if isinstance(restaurant, Restaurant):
            self._restaurant = restaurant


Review.all = []
restaurant_1 = Restaurant("Mels")
restaurant_2 = Restaurant("IronMeal")
restaurant_3 = Restaurant("Da Giovanni")
restaurant_4 = Restaurant("Mel'b")
customer = Customer("Steve", "Wayne")
customer_2 = Customer("Dima", "Bay")
Review(customer, restaurant_1, 5)
Review(customer, restaurant_2, 4)
Review(customer, restaurant_3, 3)
Review(customer, restaurant_4, 2)
Review(customer_2, restaurant_1, 5)
Review(customer_2, restaurant_2, 5)
Review(customer_2, restaurant_3, 5)


print(restaurant_1)
print(restaurant_2)
print(restaurant_3)
print(restaurant_4)
print(Restaurant.top_two_restaurants())
