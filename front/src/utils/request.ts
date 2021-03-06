import axios from 'axios'
import { Message, MessageBox } from 'element-ui'
import { UserModule } from '@/store/modules/user'
import { AppModule } from '@/store/modules/app'

const service = axios.create({
  baseURL: process.env.VUE_APP_BASE_API, // url = base url + request url
  timeout: 5000
  // withCredentials: true // send cookies when cross-domain requests
})

// Request interceptors
service.interceptors.request.use(
  config => {
    // Add X-Access-Token header to every request, you can add other custom headers here
    if (UserModule.token) {
      config.headers['X-Access-Token'] = UserModule.token

      // config.headers['Accept'] = 'application/json'
      // config.headers['Alliance-ID'] = '10000'
      // config.headers['token'] = getToken()
    }
    return config
  },
  error => {
    Promise.reject(error)
  }
)

// response interceptor
service.interceptors.response.use(
  /**
   * If you want to get http information such as headers or status
   * Please return  response => response
   */

  /**
   * Determine the request status by custom code
   * Here is just an example
   * You can also judge the status by HTTP Status Code
   */
  response => {
    const res = response.data
    return res
    // if the custom code is not 20000, it is judged as an error.
    // if (res.code !== 20000) {
    //   Message({
    //     message: res.message || 'Error',
    //     type: 'error',
    //     duration: 5 * 1000
    //   })

    //   // 50008: Illegal token 50012: Other clients logged in 50014: Token expired
    //   if (res.code === 50008 || res.code === 50012 || res.code === 50014) {
    //     // to re-login
    //     MessageBox.confirm('You have been logged out, you can cancel to stay on this page, or log in again', 'Confirm logout', {
    //       confirmButtonText: 'Re-Login',
    //       cancelButtonText: 'Cancel',
    //       type: 'warning'
    //     }).then(() => {
    //       UserModule.resetToken().then(() => {
    //         location.reload()
    //       })
    //     })
    //   }
    //   return Promise.reject(new Error(res.message || 'Error'))
    // } else {
    //   return res
    // }
  },
  error => {
    console.log('error', error) // for debug
    if (error.response) {
      // ??????????????? ???????????????401???????????????
      Message({
        message: error.response.data.message,
        type: 'error',
        duration: 5 * 1000
      })
    } else {
      Message({
        message: error.message,
        type: 'error',
        duration: 5 * 1000
      })
    }
    return Promise.reject(error)
  }
)

// // Response interceptors
// service.interceptors.response.use(
//   response => {
//     // Some example codes here:
//     // code == 20000: success
//     // code == 50001: invalid access token
//     // code == 50002: already login in other place
//     // code == 50003: access token expired
//     // code == 50004: invalid user (user not exist)
//     // code == 50005: username or password is incorrect
//     // You can change this part for your own usage.
//     const res = response.data
//     if (res.code !== 20000) {
//       Message({
//         message: res.message || 'Error',
//         type: 'error',
//         duration: 5 * 1000
//       })
//       if (res.code === 50008 || res.code === 50012 || res.code === 50014) {
//         MessageBox.confirm(
//           '????????????????????????????????????????????????????????????????????????',
//           '????????????',
//           {
//             confirmButtonText: '????????????',
//             cancelButtonText: '??????',
//             type: 'warning'
//           }
//         ).then(() => {
//           UserModule.ResetToken()
//           location.reload() // To prevent bugs from vue-router
//         })
//       }
//       return Promise.reject(new Error(res.message || 'Error'))
//       // return Promise.reject(new Error('error with code: ' + res.code))
//     } else {
//       return response.data
//     }
//   },
//   error => {
//     Message({
//       message: error.message,
//       type: 'error',
//       duration: 5 * 1000
//     })
//     return Promise.reject(error)
//   }
// )

export default service
