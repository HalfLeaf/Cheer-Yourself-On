import axios from 'axios'

const $getJson = function (method) {
    return new Promise((resolve, reject) => {
      axios({
        method: 'get',
        url: method,
        dataType: "json",
        crossDomain: true,
        cache: false
      }).then(res => {
        resolve(res)
      }).catch(error => {
        reject(error)
      })
    })
}

//获取JSON数据
const getH5StaticJson = data => {
  return $getJson('../assets/lovaTalk.json',data)
}

export default getH5StaticJson;