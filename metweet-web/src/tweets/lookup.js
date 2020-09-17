import {backendlookup} from '../lookup'


export function apitweetCreate(newTweet, callback){
    backendlookup("POST", "/tweets/create/", callback, {content: newTweet})
  }
  
  
export function apitweetList(callback) {
    backendlookup("GET", "/tweets/", callback)
  }