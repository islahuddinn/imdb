import React, { useEffect, useState } from 'react';
import axios from 'axios';

function App() {
  const [movies, setMovies] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:8000/get/');
        setMovies(response.data);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []);

  return (
    <div>
      <nav className="navbar navbar-expand-lg navbar-dark bg-dark stiky">
        <div className="container">
          <a className="navbar-brand" href="/">Mr-Movies</a>
        </div>
      </nav>
      <h1 className='d-flex justify-content-center'>Movies</h1>
        <div className='card-container row ' >
  {movies.map((api_movie) => (
    <div className='card col-4 '  key={api_movie.id}>
      <img src={`https://image.tmdb.org/t/p/original${api_movie.poster_path}`} alt={api_movie.title} />
      <h2 className='card-title'>{api_movie.title}</h2>
      <p>Original Title: {api_movie.original_title}</p>
      <p className='card-text'>Overview: {api_movie.overview}</p>
      <p>Popularity: {api_movie.popularity}</p>
      <p>Release Date: {api_movie.release_date}</p>
      <p>Vote Count: {api_movie.vote_count}</p>
    </div>
  ))}
</div>
    </div>
  );
}

export default App;

