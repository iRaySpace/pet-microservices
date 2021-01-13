import React from "react";

function ClinicReview({ rating, feedback }) {
  return (
    <div>
      <div>Rating: {rating}</div>
      <div>{feedback}</div>
    </div>
  );
}

export default ClinicReview;
