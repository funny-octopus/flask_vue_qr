var app = new Vue({
    el: '#app',
    delimiters: ['[[', ']]'],
    data: {
        ident:null,
        select_list:['category', 'factory', 'country', 'currency', 'price_v'],
        resp:null,
        items:null,
        changes_flag:true,
    },
    methods:{
        save:function(){
            console.log(this.resp.product);
            axios({
                method:'post',
                url:'/api/item/'+this.ident,
                data:this.resp.product,
                headers:{
                    "Content-type":"application/json",
                },
            })
            .then(function(response){
                console.log('ответ получен!');
                console.log(response.data);
                if(response.data.status==='ok'){
                    app.resp.product.article.value = response.data.article;
                };
            })
            .catch(function(error){
                console.log(error);
            });
            this.changes_flag=false;
        },
    },
    created(){
        this.ident = document.getElementById('ident').value;
        axios.get('/api/item/'+this.ident)
        // .then(response => (this.product = response.data.product;this.id = response.data.id;));
            .then(response => (this.resp = response.data));
        axios.get('/api/items')
            .then(response => (this.items = response.data));
    },
    beforeMount(){
    },
    mounted(){
    },

})
