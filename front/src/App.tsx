import React from "react";
import ClinicList from "./components/ClinicList";
import { useFetch } from "./hooks/useFetch";
import { usePost } from "./hooks/usePost";

function App() {
  const fetchClinic = useFetch("http://localhost:8000/clinics");
  const postReview = usePost("http://localhost:8001/reviews");

  function handleReview(id) {
    postReview.execute({
      parent: id,
      rating: 5,
      feedback: "Generic feedback",
    });
  }

  return (
    <div className="App">
      <h1>Pet Microservices</h1>
      {fetchClinic.isLoading && <div>Loading data...</div>}
      {postReview.isLoading && <div>Saving data...</div>}
      <ClinicList data={fetchClinic.data} onReview={handleReview} />
    </div>
  );
}

export default App;
