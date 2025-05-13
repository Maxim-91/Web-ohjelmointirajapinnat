// Task 3, making changes to the file code to load data dynamically instead of statically

import React, { useState, useEffect } from 'react'; //Added useEffect - for get dynamic data
import RestaurantCard from './RestaurantCard';
import './RestaurantList.css'; // Import your CSS file

function RestaurantList() {
  const [restaurants, setRestaurants] = useState([]);

  useEffect(() => 
    {
      // Get dynamic data instead of static
      fetch('http://localhost:8000/api/restaurants/ratings', 
           {headers: { accept: 'application/json' }})
       .then(res => res.json())
       .then(data => 
          {
            const formatted = data.map(item =>
           ({
             id: item.id,
             imageUrl: '/images/cheese_burger.jpg', // Taking a picture from a folder, it does not load dynamically
             name: item.name,
             averageRating: item.rating ?? 0,
             reviewCount: item.review_count,
             cuisine: item.cuisine,
             priceRange: item.price_range,
             address: item.address
            }));
          setRestaurants(formatted);
          })       
    }, []);
    
    
  return (
    <div className="restaurant-list-container">
      <div className="side-panel">
        <h3>Actions</h3>
        <button onClick={() => {}}>Add Rating</button>
        {/* Add more action buttons here */}
      </div>
      <div className="restaurant-list">
        {restaurants.map((restaurant) => (
          <RestaurantCard key={restaurant.id} restaurant={restaurant} />
        ))}
      </div>
    </div>
  );
}

export default RestaurantList;