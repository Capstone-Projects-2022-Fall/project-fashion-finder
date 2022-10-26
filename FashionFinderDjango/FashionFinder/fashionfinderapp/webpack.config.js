const path = require("path");
const webpack = require("webpack");

module.exports = {
  entry: {
    index: path.resolve('/static/jsx/index.jsx'),
    register: path.resolve('/static/jsx/register.jsx'),
  },
  output: {
    path: path.resolve(__dirname, "./static/fashionfinder"),
    filename: "[name].js",
  },
  module: {
    rules: [
      {
        test: /\.js|.jsx$/,
        exclude: /node_modules/,
        use: "babel-loader",
      },
      {
        test: /\.css$/,
        exclude: /node_modules/,
        use: ["style-loader", "css-loader"],
      },
    ],
  },
  optimization: {
    minimize: true,
  },
  plugins: [
    new webpack.DefinePlugin({
      "process.env": {
        NODE_ENV: JSON.stringify("development"),
      },
    }),
  ],
};