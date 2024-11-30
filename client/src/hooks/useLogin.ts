//Let's generate a custom hook that will handle the login logic. This hook will be used in the Login component.
import { useMutation } from "@tanstack/react-query";
import APIClient from "../api/api-client";

interface LoginResponse {
  access_token: string;
  token_type: string;
}

const apiClient = new APIClient<LoginResponse>("/login");

const useLogin = () =>
  useMutation<LoginResponse, Error, { username: string; password: string }>({
    mutationFn: async (credentials: { username: string; password: string }) =>
      apiClient.login(credentials.username, credentials.password),
  });

//
/*
const useLogin = () =>
  useMutation<LoginResponse, Error, { email: string; password: string }>({
    mutationFn: async (credentials) => {
      // Call the asynchronous API client method
      const data = await apiClient.login(
        credentials.email,
        credentials.password
      );
      return data;
    },
  });
  */

export default useLogin;
