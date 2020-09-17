import {backendlookup} from '../lookup'


export function apitweetCreate(newTweet, callback){
    backendlookup("POST", "/tweets/create/", callback, {content: newTweet})
  }


export function apitweetAction(tweetId, action, callback){
    const data = {id: tweetId, action: action}
    backendlookup("POST", "/tweets/action/", callback, data)
  }
  
  
export function apitweetList(callback) {
    backendlookup("GET", "/tweets/", callback)
  }