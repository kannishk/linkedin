const str = "...";

let res = {};

str.replace(/([^\s,=]+)=([^,]+)(?=,|$)/g, function ($0, key, value) {
  res[key] = value;
});

console.log(res);
