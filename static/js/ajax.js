//Update artist from backed, capture event
const btnHome = document.getElementById("logo_container");
const btnAddArtist = document.getElementById("add_new_artist");
const urlArtist = "/artist"; // url
const urlAddArtist = "/add_artist"; // url
const rowsTable = document.getElementsByClassName("row_table_list_artist");

btnHome.addEventListener("click", function () {
  window.location.href = "/";
});
// ---------------------------------------------------------------------------------------------

function requestAjax(dataSent, url, type) {
  $.ajax({
    url: url,
    type: type,
    data: { search: dataSent }, // This data is the artist name
    success: function (response) {
      // Update the dynamic content
      $("#dynamic-content").html(response);
    },
    error: function (error) {
      console.error("Error in the POST request:", error);
    },
  });
}
// ---------------------------------------------------------------------------------------------

// Build new artist url
function buildArtistUrl(code) {
  nameUrlFormat = code;
  for (let i = 0; i < code.length; i++) {
    if (code[i] === " ") {
      nameUrlFormat = nameUrlFormat.replace(" ", "_");
    }
  }
  let newUrl = urlArtist + "/" + encodeURIComponent(nameUrlFormat);
  window.history.pushState({ path: newUrl }, "", newUrl); // Update the URL in browser
}
// ---------------------------------------------------------------------------------------------

// Change "DOM" page according to change the url
window.addEventListener("popstate", function (event) {
  $.ajax({
    url: window.location.pathname,
    // The header is very import for execute the function correct on the server side
    headers: {
      "X-Requested-With": "popstate_event",
    },
    type: "GET",
    success: function (response) {
      $("#dynamic-content").html(response);
    },
    error: function (error) {
      console.error("Error in the GET request:", error);
    },
  });
});
// ---------------------------------------------------------------------------------------------

// Add the click event to the each row in the table
function handleClickRow(param) {
  for (const row of param) {
    row.addEventListener("click", function () {
      // Get data from the row
      let artistAka = row.cells[0].textContent;
      requestAjax(artistAka, urlArtist, "POST");
      buildArtistUrl(artistAka);
    });
  }
}
handleClickRow(rowsTable);
// ---------------------------------------------------------------------------------------------

// Add new artist
btnAddArtist.addEventListener("click", function() {
  // Get the current path
  let newUrl = "/add_artist";
  
  window.history.pushState("", "", newUrl); // Update the URL in browser
  requestAjax(null, urlAddArtist,"GET")
  location.reload();
});
// ---------------------------------------------------------------------------------------------
