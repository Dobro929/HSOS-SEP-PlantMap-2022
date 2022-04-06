import axios from "axios";

const baseURL = "http://127.0.0.1:8080/beds";

export async function getBeds() {
  const response = await axios.get(baseURL);
  return response.data;
}

export async function getBedDetail(id: string) {
  const response = await axios.get(baseURL + "/" + id);
  return response.data;
}
