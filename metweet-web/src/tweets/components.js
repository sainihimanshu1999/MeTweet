import React, {useState}  from 'react'
import {ActionBtn} from './buttons'
import {TweetsList} from './list'
import {apitweetCreate ,apitweetList} from './lookup'
import {TweetCreate} from './create'


export function TweetsComponent(props) {
    const [newTweets, setNewTweets] = useState([])
    const canTweet = props.canTweet === false ? false : true
    //backend api response 
    const handleNewTweet = (newTweet) =>{
      let tempNewTweets = [...newTweets]
      tempNewTweets.unshift(newTweet)
      setNewTweets(tempNewTweets)
    }
    return <div className={props.className}>
            {canTweet === true && <TweetCreate didTweet={handleNewTweet} className='col-12 mb-3'/>}
        <TweetsList newTweets={newTweets} {...props} />
    </div>
}


