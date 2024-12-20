import express from "express";
import mongoose from "mongoose";
import { createClient } from "redis";

const app = express();

const client = await createClient()
  .on("error", (err) => console.log("Redis Client Error", err))
  .connect();

// MongoDB Connection
mongoose
  .connect("mongodb://127.0.0.1:27017/")
  .then(() => {
    console.log("Connected to MongoDB successfully");
  })
  .catch((error) => {
    console.error("Error connecting to MongoDB:", error.message);
  });

// Event listeners for debugging connection state
mongoose.connection.on("connected", () => {
  console.log("Mongoose connected to DB");
});

mongoose.connection.on("error", (err) => {
  console.error("Mongoose connection error:", err);
});

mongoose.connection.on("disconnected", () => {
  console.log("Mongoose disconnected from DB");
});

const productSchema = new mongoose.Schema({
  name: String,
  description: String,
  price: Number,
  category: String,
  specs: Object,
});

const Product = mongoose.model("Product", productSchema);

app.get("/api/products", async (req, res) => {
  const key = generateCacheKey(req);
  const cachedProducts = await client.get(key);
  if (cachedProducts) {
    console.log("Fetching Cached Data");
    return res.json(JSON.parse(cachedProducts));
  }
  console.log("Fetching New Data");

  const query = {};
  if (req.query.category) {
    query.category = req.query.category;
  }
  const products = await Product.find(query);
  if (products.length) {
    await client.set(key, JSON.stringify(products));
  }
  res.json(products);
});

function generateCacheKey(req) {
  const baseUrl = req.path.replace(/^\/+|\/+$/g, "").replace(/\//g, ":");
  const params = req.query;
  const sortedParams = Object.keys(params)
    .sort()
    .map((key) => `${key}=${params[key]}`)
    .join("&");

  return sortedParams ? `${baseUrl}:${sortedParams}` : baseUrl;
}

// Start Express Server
app.listen(3000, () => {
  console.log("Server started on port 3000");
});
