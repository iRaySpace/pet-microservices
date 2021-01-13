import React from "react";
import ClinicView from "./ClinicView";

function ClinicList({ data, onReview }) {
  return (
    <div>
      {data.map((row) => (
        <ClinicView key={row.id} data={row} onReview={onReview} />
      ))}
    </div>
  );
}

export default ClinicList;
