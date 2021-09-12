var appp = new Vue({
    el:'#app',
    delimiters:['[[',']]'],
    data:{
        items:[],
        link_back:false,
        cur_cat:'category',
        filt:'',

    },
    watch:{
        filt:function(newFilt){
            console.log(newFilt);
        },
    },
    computed:{
        filtred_items:function(){
            var f = this.filt;
            console.log('1');
            return this.items.filter(function(elem){
                if(f==='')return true;
                else return elem.name.indexOf(f) > -1 || elem.article.indexOf(f) > -1;
            });
        },
    },
    methods:{
        get_items:function(id){
            this.cur_cat = 'product';
            this.link_back = true;
            axios.get('/api/products/'+id)
                    .then(response => this.items = response.data.items);
        },
        change_cur_cat:function(){
            this.cur_cat = 'category';
            this.link_back = false;
            this.filt = '';
            axios.get('/api/category/')
                .then(response => this.items = response.data.items);
        },
        redirect_to_item:function(product_id){
            window.location.replace('/item/' + product_id);
        },
    },
    beforeCreate(){
        axios.get('/api/category/')
            .then(response => this.items = response.data.items);
    },


})
