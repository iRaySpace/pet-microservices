import { useState, useEffect } from "react";
import axios from "axios";

export const useFetch = (url: string) => {
  const [isLoading, setLoading] = useState(false);
  const [data, setData] = useState([]);

  useEffect(() => {
    setLoading(true);
    axios
      .get(url)
      .then((res) => setData(res.data))
      .finally(() => setLoading(false));
  }, [url]);

  return { data, isLoading };
};
