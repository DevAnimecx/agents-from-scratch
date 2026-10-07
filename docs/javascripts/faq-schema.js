(function () {
  if (location.pathname.endsWith("/") || location.pathname.endsWith("index.html")) {
    const script = document.createElement("script");
    script.type = "application/ld+json";
    script.textContent = JSON.stringify({"@context":"https://schema.org","@type":"Course","name":"agents-from-scratch","description":"Build production AI agents from first principles in raw Python.","provider":{"@type":"Organization","name":"agents-from-scratch"},"educationalLevel":"Intermediate"});
    document.head.appendChild(script);
  }
})();
