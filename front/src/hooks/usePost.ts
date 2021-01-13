import { useState, useEffect } from "react";
import axios from "axios";

export const usePost = (url: string) => {
  const [isLoading, setLoading] = useState(false);
  const [data, setData] = useState({});
  function execute(requestData: any) {
    setLoading(true);
    axios
      .post(url, requestData)
      .then((res) => setData(res.data))
      .finally(() => setLoading(false));
  }
  return { isLoading, data, execute };
};
