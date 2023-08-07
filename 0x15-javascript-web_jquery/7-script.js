$.get(
  "https://swapi-api.alx-tools.com/api/people/5/?format=json",
  function (dataN) {
    $("DIV#character").text(dataN["name"]);
  }
);
