console.log("-- tweets script loaded")

const xhr = new XMLHttpRequest()
const method = "GET"
const url = "/tweet/list"
const responseType = "json"
let tweetsElement = document.getElementById("tweets")


xhr.responseType = responseType
xhr.open(method, url)
xhr.onload = () => {
    let serverResponse = xhr.response
    let tweetArray = serverResponse.data

    let tweetStr = ""
    tweetArray.forEach(e => {
        console.log(e.img.url)
        tweetStr += htmlCreator(e)
    })
    tweetsElement.innerHTML = tweetStr

}
xhr.send()

let htmlCreator = (e) => {
    let tweetStr = ""
    tweetStr += `
        <h2>${e.pk}</h2> 
        <p>${e.content}</p> 
        <p><button onClick="likeBtn(${e.pk}, ${e.like})" type="button" class="btn btn-light">like ${e.like}</button></p>
        <img src="{{ ${e.img.url} }}" alt=""> <br>
                `
    return tweetStr
}

let likeBtn = (pk, like) => {
    // got pk of tweet
    console.log(pk)
}