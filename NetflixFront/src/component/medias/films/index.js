import React, {useState, useEffect} from 'react'
import axios from 'axios'

const Films = (props) =>{


    const [filmList, setFilm] = useState([])
    const axios = require('axios');

     /* Hugo-Jean EGU */
    useEffect( () => {
        axios({
            method: 'get',
            url: "http://127.0.0.1:5000/films/",
            params: {
            'idUser': "6246f87f7f202b2db842d679"
            }
        })
        .then(res => {
            setFilm(res.data)
        })
        .catch(err => {
            console.log(err);
        })

    }, [])


    return(
        <div>
                {filmList.map((item) => (
                    <div key={item.id}>
                        <p>{item.title}</p>
                    </div>

                ))}
        </div>
    )
}

export default Films