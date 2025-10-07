document.getElementById("gen").onclick = async () => {
  const idea = document.getElementById("idea").value;
  const tone = document.getElementById("tone").value;
  const res = await fetch("/generate", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ idea, tone })
  });
  const data = await res.json();
  const images = data.images;
  const container = document.getElementById("result");
  container.innerHTML = "";
  images.forEach((b64) => {
    const img = document.createElement("img");
    img.src = "data:image/png;base64," + b64;
    img.style.width = "220px";
    img.style.margin = "8px";
    container.appendChild(img);
  });
};
