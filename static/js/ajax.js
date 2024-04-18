//Update artist from backed, capture event
const btnHome = document.getElementById("logo_container");
const btnAddArtist = document.getElementById("add_new_artist");
const rowsTable = document.getElementsByClassName("row_table_list_artist");
const login = document.getElementById("login_link_footer");
const logout = document.getElementById("logout_link_footer");
const urlRoot = "/"; // url
const urlArtist = "/artist"; // url
const urlAddArtist = "/add_artist"; // url
const urlLogin = "/login"; // url
const urlLoginAccess = "/login_verification"; // url
const urlLogOut = "/logout"; // url

// click in logo for redirect to home
btnHome.addEventListener("click", function () {
  window.location.href = "/";
});
// ---------------------------------------------------------------------------------------------

// Function ajax for general use
function requestAjax(dataSent, url, type) {
  $.ajax({
    headers: {
      "Content-Type": "application/json",
    },
    url: url,
    type: type,
    data: JSON.stringify({ search: dataSent }),
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
try {
  btnAddArtist.addEventListener("click", function () {
    // Get the current path
    let newUrl = urlAddArtist;

    window.history.pushState("", "", newUrl); // Update the URL in browser
    requestAjax(null, urlAddArtist, "GET");
    location.reload();
  });
} catch (error) {
}
// ---------------------------------------------------------------------------------------------

// Login link form
try {
  login.addEventListener("click", function () {
    let newUrl = urlLogin;

    window.history.pushState("", "", newUrl);
    requestAjax(null, urlLogin, "GET");
    location.reload();
  });
} catch (error) {
}

// ---------------------------------------------------------------------------------------------

// Logout link
try {
  logout.addEventListener("click", function () {
    $.ajax({
      url: urlLogOut,
      type: "GET",
      success: function (response) {
        location.reload();
        window.location.href = "/";
      },
      error: function (error) {
        console.error("Error in the GET request:", error);
      },
    });
  });
} catch (error) {
}

// ---------------------------------------------------------------------------------------------

// Login
function handleFormSubmit(event) {
  event.preventDefault(); // avoid the form submit
  let inputUser = document.getElementById("login_input_user");
  let inputPass = document.getElementById("login_input_pass");
  let username = inputUser.value;
  let password = inputPass.value;

  credentials = {
    user: username,
    pass: password,
  };

  $.ajax({
    headers: {
      "Content-Type": "application/json",
    },
    url: urlLoginAccess,
    type: "POST",
    data: JSON.stringify({ search: credentials }),

    success: function (response) {
      console.log(response);
      if (response != "") {
        window.location.href = "/";
      } else {
        document.getElementById("login_log").style.display="inline";
        console.log("no user");
      }
    },
    error: function (error) {
      console.error("Error in the POST request:", error);
    },
  });
}

$("#login_form").submit(handleFormSubmit);
// ---------------------------------------------------------------------------------------------
