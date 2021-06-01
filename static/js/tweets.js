console.log("-- tweets script loaded")

const xhr = new XMLHttpRequest()
const method = "GET"
const url = "/tweet/list"
const responseType = "json"
let tweetsElement = document.getElementById("tweets")


xhr.responseType = responseType
xhr.open(method, url)
xhr.onload = () => {
    // catch json from url
    let serverResponse = xhr.response
    let tweetArray = serverResponse.data
    tweetsElement.innerHTML = htmlCreator(tweetArray)

}
xhr.send()

let htmlCreator = (dataList) => {
    // generate html output in string format with tweet data
    let tweetStr = ""
    dataList.forEach(e => {

        tweetStr += `
        <div class="jumbotron" style="background-color: rgba(234,234,234,0.28)">
            <h2>${e.pk}</h2> 
            <p>${e.content}</p> 
            <p><button onClick="likeBtn(${e.pk}, ${e.like})" type="button" class="btn btn-light">like ${e.like}</button></p>
            <p> image : ${e.img.url} ,url not working</p>
            <img src="{{ ${e.img.url} }}" alt=""> <br>
        </div>
                `
    })
    return tweetStr
}

let likeBtn = (pk, like) => {
    // got pk of tweet
    console.log(pk)
}