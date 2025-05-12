// src/components/Resumes.js
import React, { useEffect, useState } from 'react';
import axios from 'axios';

const Resumes = () => {
  const [resumes, setResumes] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Fetch resumes from backend when component mounts
  useEffect(() => {
    const fetchResumes = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/resumes/');
        setResumes(response.data);
        setLoading(false);
      } catch (error) {
        setError('Error fetching resumes');
        setLoading(false);
      }
    };

    fetchResumes();
  }, []);

  if (loading) {
    return <div>Loading resumes...</div>;
  }

  if (error) {
    return <div>{error}</div>;
  }

  return (
    <div>
      <h1>Resumes</h1>
      <ul>
        {resumes.length > 0 ? (
          resumes.map(resume => (
            <li key={resume.id}>
              <h3>{resume.name}</h3>
              <p><strong>Skills:</strong> {resume.skills}</p>
              <p><strong>Experience:</strong> {resume.experience}</p>
              <p><strong>Projects:</strong> {resume.projects}</p>
              <p><strong>Certifications:</strong> {resume.certifications}</p>
            </li>
          ))
        ) : (
          <p>No resumes available</p>
        )}
      </ul>
    </div>
  );
};

export default Resumes;
