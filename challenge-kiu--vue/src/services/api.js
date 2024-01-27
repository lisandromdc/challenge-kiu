import axios from "axios";

const request = axios.create({
  baseURL: "https://api.tvmaze.com",
});

export default {
  get(url) {
    return request.get(url);
  },
};
