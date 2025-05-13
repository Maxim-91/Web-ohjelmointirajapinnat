// Tehtävä 4
// A) Arviointien listaus (25p)
// B) Valitun arvioin poisto (25p)

import { useParams } from 'react-router-dom';
import { useEffect, useState } from 'react';
import StarRating from './StarRating'; // Import to display stars in reviews (for use className="star-rating")

function RatingsByRestaurant() {
  const { id } = useParams();
  const [ratings, setRatings] = useState([]);
  const [error, setError] = useState(null);

  // Use GET from http://localhost:8000/docs for ratings, Tehtävä 4a
  useEffect(() => {
    fetch(`http://localhost:8000/api/restaurants/${id}/ratings`, {
      headers: { accept: 'application/json' }
    })
      .then(res => res.json())
      .then((data) => setRatings(data))      
  }, [id]); 

  // Tehtävä 4b: Valitun arvioin poisto
  const handleDelete = (ratingId) => 
    {
        fetch(`http://localhost:8000/api/restaurants/${id}/ratings/${ratingId}`, 
            { method: 'DELETE'});
        setRatings(prev => prev.filter(r => r.id !== ratingId));
    };

// Display the restaurant ratings, Tehtävä 4a
return ( 
    <div>       
      <h2>Restaurant Ratings №{id}</h2>       
      {ratings.length === 0 ? (<p>No ratings found.</p>) : 
      (        
        ratings.map((rating) => (
            <div key={rating.id}>
                <div className="star-rating" style={{ display: 'flex', justifyContent: 'space-between' }}>
                    <StarRating rating={rating.value} />
                    <button onClick={() => handleDelete(rating.id)}>Delete</button>
                </div>
                <p>{rating.description}</p>
                <p style={{ fontSize: '0.9em', color: 'gray' }}>Date:{rating.date_rated}</p>
                <hr/>
            </div>
        ))
      )}    
    </div>
  );
}

export default RatingsByRestaurant;