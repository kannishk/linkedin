import fetch from "node-fetch";
import { promises as fs } from "fs";

const data = JSON.parse(await fs.readFile("./people.json", "utf-8"));
const filteredData = [];

const checkIfOpenToWork = async (publicId) => {
  const a = await fetch("https://www.linkedin.com/in/" + publicId, {
    headers: {
      accept:
        "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
      "accept-language": "en-GB;q=0.5",
      "cache-control": "max-age=0",
      "sec-fetch-dest": "document",
      "sec-fetch-mode": "navigate",
      "sec-fetch-site": "same-origin",
      "sec-fetch-user": "?1",
      "sec-gpc": "1",
      "upgrade-insecure-requests": "1",
      cookie: "...",
    },
    referrerPolicy: "strict-origin-when-cross-origin",
    body: null,
    method: "GET",
  });

  const data = await a.text();
  if (data.includes("OPEN_TO_WORK")) {
    return true;
  } else {
    return false;
  }
};

// console.log(await checkIfOpenToWork("pallavi-chauhan-ba6a99193"));
// console.log(await checkIfOpenToWork("sandip-ranjan-behera-a89b5b205"));
// pallavi-chauhan-ba6a99193
let count = 0;
for (const user of data) {
  try {
    if (await checkIfOpenToWork(user.public_id)) {
      console.log("Found ", user.public_id);
      count++;
      filteredData.push(user);
    } else {
      console.log(`${user.public_id} NOT OPEN TO WORK`);
    }
  } catch (e) {
    console.log("Got some error", e.message);
    continue;
  }
}
console.log(count);

await fs.writeFile("filtered.json", JSON.stringify(filteredData));
