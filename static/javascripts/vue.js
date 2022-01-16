import {fetchGET, fetchPOST} from './api.js'

window.addEventListener('DOMContentLoaded', () => {
  new Vue({
    el: '#app',
    delimiters: ['[[', ']]'],
    data() {
      return {
        contentImages: data.contentImages,
        comments: data.comments,
        comment: '',
        imageContainerStyle: {},
        isShowMoreBtn: true,
        isValidateComment: false,
      }
    },
    methods: {
      swipeImage(e, index) {
        const imageWidth = e.target.offsetWidth
        const isRight = imageWidth / 2 < e.offsetX

        const nextIndex = isRight ? index + 1 : index - 1
        if (nextIndex < 0 || nextIndex >= this.contentImages.length) return

        const swipeX = imageWidth * -nextIndex
        this.imageContainerStyle = {transform: `translateX(${swipeX}px)`}
      },
      checkFetchOk(status) {
        if (status !== 200) {
          alert('ERROR')
          return false
        }
        return true
      },
      async getComments() {
        const {status, data} = await fetchGET(urls.getCommentsApi)
        if (!this.checkFetchOk(status)) return

        this.isShowMoreBtn = false
        this.addComments(data.comments)
      },
      addComments(comments) {
        this.comments = [...this.comments, ...comments]
      },
      validateComment(e) {
        this.comment = e.target.value

        this.isValidateComment = this.comment ? true : false
      },
      async submitComment(e) {
        if (!this.isValidateComment) return

        const {status, data} = await fetchPOST(urls.postCommentApi, {
          comment: this.comment,
          user
        })
        if (!this.checkFetchOk(status)) return

        this.addComments([{
          id: data.id,
          text: this.comment,
          user
        }])
        this.comment = ''
      }
    }
  })
})
