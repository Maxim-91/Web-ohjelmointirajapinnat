import { useParams } from 'react-router-dom';


function RatingsByRestaurant() {
    const {id} = useParams();

    return (<p>terve {id}</p>)
}

export default RatingsByRestaurant;