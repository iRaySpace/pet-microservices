import React from "react";
import ClinicReview from "./ClinicReview";
import { useFetch } from "../hooks/useFetch";

function ClinicView({ data, onReview }) {
  const { data: reviewData, isLoading } = useFetch(
    `http://localhost:8001/reviews/${data.id}`
  );
  return (
    <div>
      {data.name}
      {isLoading && <div>Loading</div>}
      {!isLoading &&
        reviewData.map((review) => (
          <ClinicReview
            key={review.id}
            rating={review.rating}
            feedback={review.feedback}
          />
        ))}
      <button onClick={() => onReview(data.id)}>Give Review</button>
    </div>
  );
}

export default ClinicView;
