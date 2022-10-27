const path = require("path");
const webpack = require("webpack");
const ESLintPlugin = require('eslint-webpack-plugin');

module.exports = {
  entry: {
    index: path.resolve('/static/jsx/index.jsx'),
    home: path.resolve('static/jsx/home.jsx'),
    register: path.resolve('/static/jsx/register.jsx'),
    navbar: path.resolve('/static/jsx/navbar.jsx'),
  },
  mode: 'development',
  output: {
    path: path.resolve(__dirname, "./static/fashionfinder"),
    filename: "[name].js",
  },
  module: {
    rules: [
      {
        test: /\.m?jsx?$/,
        exclude: /node_modules/,
        use: [{loader: "babel-loader", options: {
          "presets": [
            "@babel/preset-env",
            "@babel/preset-react"
          ],
          "plugins": [
            ["@babel/plugin-transform-react-jsx", { "pragma":"React.createElement", "pragmaFrag":"React.Fragment" }],
            ["@babel/plugin-proposal-class-properties", { "loose": true }],
            ["@babel/plugin-proposal-private-methods", { "loose": true }],
            ["@babel/plugin-proposal-private-property-in-object", { "loose": true }],
            "@babel/plugin-proposal-optional-chaining"
          ]
        }}]
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
  plugins: [new ESLintPlugin({})],
  resolve: {
    alias: {
      jsx: path.resolve('jsx/'),
    },
    extensions: [".js", ".jsx", ".json"],
    mainFields: ["browser", "module", "main", "style"]
  },
};