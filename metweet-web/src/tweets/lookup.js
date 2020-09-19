import {backendlookup} from '../lookup'


export function apitweetCreate(newTweet, callback){
    backendlookup("POST", "/tweets/create/", callback, {content: newTweet})
  }


export function apitweetAction(tweetId, action, callback){
    const data = {id: tweetId, action: action}
    backendlookup("POST", "/tweets/action/", callback, data)
  }
  
export function apitweetDetail(tweetId, callback) {
    backendlookup("GET", `/tweets/?${tweetId}/`, callback)
  }


  
export function apitweetList(username, callback) {
    let endpoint = "/tweets/"
    if(username){
      endpoint = `/tweets/?username=${username}`
    }
    backendlookup("GET", endpoint, callback)
  }