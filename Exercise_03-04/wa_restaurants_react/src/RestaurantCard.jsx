import React from 'react';
import './RestaurantCard.css'; // Import your CSS file
import StarRating from './StarRating'; // Assuming you have a StarRating component
import { Link } from 'react-router-dom';

function RestaurantCard({ restaurant, onRemoveRating }) {
  return (
    <div className="restaurant-card">
      <div className="card-left">
        <img src={restaurant.imageUrl} alt={restaurant.name} className="restaurant-image" />
      </div>
      <div className="card-right">
        <div className="card-right-content"> {/* New container for text content */}
          <h3 className="restaurant-name">
            <strong><Link to={`/${restaurant.id}`}>{restaurant.name}</Link></strong>
          </h3>
          <div className="restaurant-rating">
            <StarRating rating={restaurant.averageRating} />
            <span>{restaurant.averageRating} ({restaurant.reviewCount} reviews)</span>
          </div>
          <p className="restaurant-details">
            <span>{restaurant.cuisine}</span><span>{restaurant.priceRange}</span>
          </p>
          <p className="restaurant-address">{restaurant.address}</p>
        </div>
        {restaurant.averageRating > 0 && (
          <button className="remove-rating-button-right" onClick={() => onRemoveRating(restaurant.id)}>
            Remove
          </button>
        )}
      </div>
    </div>
  );
}

export default RestaurantCard;