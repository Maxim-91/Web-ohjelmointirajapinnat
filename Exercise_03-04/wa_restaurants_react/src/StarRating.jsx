import React from 'react';
import './StarRating.css'; // Create a StarRating.css if you want custom star styles

function StarRating({ rating }) {
  const fullStars = Math.floor(rating);
  const hasHalfStar = rating % 1 !== 0;
  const emptyStars = 5 - fullStars - (hasHalfStar ? 1 : 0);

  const stars = [];
  for (let i = 0; i < fullStars; i++) {
    stars.push(<span key={`full-${i}`} className="star full-star">★</span>);
  }
  if (hasHalfStar) {
    stars.push(<span key="half" className="star half-star">½</span>);
  }
  for (let i = 0; i < emptyStars; i++) {
    stars.push(<span key={`empty-${i}`} className="star empty-star">☆</span>);
  }

  return <div className="star-rating">{stars}</div>;
}

export default StarRating;