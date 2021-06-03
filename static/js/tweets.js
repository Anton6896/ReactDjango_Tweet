console.log("-- loaded at home page start ")

/**
 * rendering html tweets list to home page
 * function loads at home page start
 * @param tweetsEl  list of all tweets at the page
 */
let loadTweets = (tweetsEl) => {
    const xhr = new XMLHttpRequest()
    const method = "GET"
    const url = "list"
    xhr.responseType = "json"

    xhr.open(method, url)
    xhr.onload = () => {
        // catch json from url
        let serverResponse = xhr.response
        let tweetArray = serverResponse.data
        tweetsEl.innerHTML = htmlCreatorUtil(tweetArray)
    }

    xhr.send()
}

// load all tweets at page start up
let tweetList = document.getElementById("tweetList")
loadTweets(tweetList)

/**
 * util for creating html elements
 * @param dataList list of tweet objects
 * @returns {string} in html format
 */
let htmlCreatorUtil = (dataList) => {
    // generate html output in string format with tweet data
    let tweetStr = ""
    for (let i of dataList.entries()) {
        tweetStr += `
            <div class="jumbotron" style="background-color: rgba(234,234,234,0.28)">
                <h2>${i[1].pk}</h2> 
                <p>${i[1].content}</p> 
                <p><button onClick="likeBtn(${i[1].pk}, ${i[1].like})" type="button" class="btn btn-success">like ${i[1].like}</button></p>
                <img style="width: auto; height: 5vw" src="${i[1].img}" alt="">
            </div>
                    `
    }
    return tweetStr
}

/**
 * add or remove like to tweet
 * @param pk tweet pk
 * @param like amount of likes on this tweet
 */
let likeBtn = (pk, like) => {
    // got pk of tweet
    console.log(pk)
}

/**
 * creating new tweet and load all tweet at the home page again
 * @type {HTMLElement} tweet creation form
 */
let tweetForm = document.getElementById("tweet_create_form")
tweetForm.addEventListener("submit", (e) => {
    e.preventDefault();
    let target = e.target
    let formData = new FormData(target)
    let url = target.getAttribute("action")
    let method = target.getAttribute("method")
    let xhr = new XMLHttpRequest();
    xhr.open(method, url);
    // setRequestHeader -> will allow to Django understand that this is Ajax forms request
    xhr.setRequestHeader("HTTP_X_REQUESTED_WITH", "XMLHttpRequest")
    xhr.setRequestHeader("X-Requested-With", "XMLHttpRequest")
    xhr.onload = () => {
        console.log(xhr.response)
        loadTweets(tweetList)
    }
    xhr.send(formData)
})
