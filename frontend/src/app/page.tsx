import axios from "axios";

export default async function Home() {
  const response = await axios.get("http://backend:7860");
  const data = await response.data

  return <div>{data.Hello}</div>;
}
