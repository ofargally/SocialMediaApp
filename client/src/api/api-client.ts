import axios from "axios";

const axiosInstance = axios.create({
  baseURL: "http://127.0.0.1:8000",
  timeout: 10000,
});

class APIClient<T> {
  endpoint: string;
  constructor(endpoint: string) {
    this.endpoint = endpoint;
  }
  // we are going to work on the log in endpoint
  login = async (email: string, password: string) => {
    const formData = new FormData();
    formData.append("email", email);
    formData.append("password", password);
    return axiosInstance
      .post<T>(this.endpoint + "/login", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      })
      .then((response) => response.data);
  };
}

export default APIClient;
