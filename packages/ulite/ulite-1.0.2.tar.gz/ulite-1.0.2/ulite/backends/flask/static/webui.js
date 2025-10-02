class UI{

    constructor(uitag, rootid, pcmd, papi) {
        this.ui_tag = uitag
        this.root_id = rootid
        this.root = document.getElementById(rootid);
        this.pcmd = pcmd;
        this.papi = papi;
        this.err_count = 0;
        this.handshaking = true;
        this.lock_drawImage = false;
        this.timestamp_base = 0;
    }

    show(){
        this.start_cmd_loop();
        this.handshaking = true;

        let block_default_keycodes = [37, 38, 39, 40, 32, 9, 18]
        document.addEventListener('keydown', (e)=>{
            if(block_default_keycodes.includes(e.keyCode)){
                e.preventDefault();
            }

        });
        document.addEventListener('keyup', (e)=>{
            if(block_default_keycodes.includes(e.keyCode)){
                e.preventDefault();
            }

        });
        requestAnimationFrame(this.newpage_loop.bind(this));
    }

    newpage_loop(){
        if (this.handshaking){
            this.api(['handshake', null]);
            requestAnimationFrame(this.newpage_loop.bind(this));
        }else{
            // 执行一次
            this.api(['newpage', null]);
            this.api(['init_window_size', [window.innerWidth, window.innerHeight]]);
            let that = this;
            window.addEventListener('resize', function() {
                // 处理窗口大小变化的代码
                that.api(['window_size', [window.innerWidth, window.innerHeight]])
            });
        }
        // this.api(['window_size', [window.innerWidth, window.innerHeight]])
        // resize

    }

    start_cmd_loop(){
        requestAnimationFrame(this.cmd_loop.bind(this))
    }

    api(list_obj, after=()=>{}){
        fetch(this.papi, {
				method: 'POST',
				headers: { 'Content-Type': 'application/json' },
				body: JSON.stringify(list_obj)
			})
			.then(response => response.json())
			.then(data => {
                after();
			});
    }

    cmd_system(method, args){
        switch (method){
            case "flash":
                window.location.reload();
                break;
            case "handshake":
                this.handshaking = false;
                let that = this
                // console.log(args)
                that.timestamp_base = args - Date.now()/1000
                console.log(that.timestamp_base)
                setInterval(() => {
                    that.api(['heartbeat', Date.now()/1000])
                }, 1000);
                break;
        }
    }

    cmd_target(target, method, args){
        let that = this;

        if (target == null){
            console.log('[error] no target: ', target, method);
            return ;
        }

        function setElementEvents(element, event_map){
            //if (Object.keys(event_map).length == 0){return;}
            let element_id = null;
            if (element==document){
                element_id = that.ui_tag;
            }else{
                element_id = element.id
            }

            function getAttr(it, path){
                let ret = it;
                for (let p of path.split(".")){
                    ret = ret[p.trim()];
                    if(ret==null){
                        return null;
                    }
                }
                return ret;
            }

            function sendEvent(e, okey, attr_map){
                let ret = {};
                let base_ret = {
                    event_type: okey,
                    target_id: element_id,
                    timestamp: e._ul_timestamp // 转换为python时间戳
                }
                for (let aokey in attr_map){
                    if (aokey == 'target_id'){
                        base_ret['target_id'] = attr_map[aokey];
                    }else{
                        ret[aokey] = getAttr(e, attr_map[aokey]);
                    }
                }
                that.api(['event', {...base_ret, ...ret}]);
            }

            for (let okey in event_map){
                if (okey == 'resize'){
                    const observer = new ResizeObserver((entries) => {
                        entries.forEach((entry) => {
                            const rect = entry.target.getBoundingClientRect();
                            that.api(['event', {
                                event_type: okey,
                                target_id: element_id,
                                left: rect.left,
                                top: rect.top,
                                width: rect.width,
                                height: rect.height
                            }]);
                        });
                    });
                    observer.observe(element);
                }

                let [fkey, attr_map] = event_map[okey];
                if(['', 'null', 'none'].includes(fkey.toLowerCase())){
                    continue;
                }

                if(['keydown', 'keyup'].includes(fkey)){
                    element._ul_keydowns = {};
                    element._ul_keyups = {};
                }

                if(fkey=='mousemove'){
                    element._ul_mousemoves = [];
                }

                let last_mouse_move = 0; // Date.now()

                element.addEventListener(fkey, (e)=>{
                    // console.log(e)
                    let curtime = Date.now();
                    e._ul_timestamp = curtime/1000 + that.timestamp_base;
                    switch(e.type){
                        // 降低mousemove事件回报率, 添加鼠标移动加速度返回
                        case 'mousemove':
                            if(e.target._ul_mousemoves.length==0){
                                e.ax = 0;
                                e.ay = 0;
                                e.vx = 0;
                                e.vy = 0;
                                e.target._ul_mousemoves.push(e);
                                return;
                            }else{
                                let el = e.target._ul_mousemoves[e.target._ul_mousemoves.length - 1]
                                let timedelta = e._ul_timestamp - el._ul_timestamp
                                if(timedelta==0){
                                    timedelta=1;
                                };
                                e.dx = e.movementX;
                                e.dy = e.movementY;
                                e.vx = e.movementX / 1000 / timedelta;
                                e.vy = e.movementY / 1000 / timedelta;
                                e.ax = (e.vx - el.vx) / timedelta;
                                e.ay = (e.vy - el.vy) / timedelta;
                                // console.log(e.ax);
                                if(curtime - last_mouse_move > 20 || Math.abs(e.ax)>10000 || Math.abs(e.ay)>10000 ){
                                    let dx = 0;
                                    let dy = 0;
                                    for(let et of e.target._ul_mousemoves){
                                        dx += et.movementX;
                                        dy += et.movementY;
                                    }
                                    e.dx = dx;
                                    e.dy = dy;
                                    e.vx = dx /1000 / (e._ul_timestamp - e.target._ul_mousemoves[0]._ul_timestamp);
                                    e.vy = dy / 1000 / (e._ul_timestamp - e.target._ul_mousemoves[0]._ul_timestamp);
                                    e.target._ul_mousemoves = [e];
                                    last_mouse_move = curtime;
                                    break;
                                }else{
                                    e.target._ul_mousemoves.push(e);
                                    return;
                                };
                            };

                            /*
                            if(mousemoves.length==0 || curtime - mousemoves[mousemoves.length - 1]._ul_timestamp > 30){

                            }

                            if(curtime - last_mouse_move < 30){
                                e.target._ul_mouse_movenentX = e.movementX + (e.target._ul_mouse_movenentX || 0)
                                e.target._ul_mouse_movenentY = e.movementY + (e.target._ul_mouse_movenentY || 0)
                                return;
                            };
                            if ('_ul_mouse_move_timeStamp' in e.target){
                                let timedelta = e.timeStamp - e.target._ul_mouse_move_timeStamp
                                if (timedelta > 0){
                                    e.vx = (e.movementX + (e.target._ul_mouse_movenentX || 0))/timedelta;
                                    e.vy = (e.movementY + (e.target._ul_mouse_movenentY || 0))/timedelta;
                                }else{
                                    e.vx = 0;
                                    e.vy = 0;
                                }

                            }else{
                                e.vx = 0;
                                e.vy = 0;
                            }
                            e.target._ul_mouse_movenentX = 0;
                            e.target._ul_mouse_movenentY = 0;
                            e.target._ul_mouse_move_timeStamp = e.timeStamp;
                            last_mouse_move = curtime;
                            break;*/

                        // 修正重复触发
                        case 'keydown':
                            element._ul_keydowns[e.keyCode] = curtime;
                            if ((e.keyCode in element._ul_keyups) && (curtime - element._ul_keyups[e.keyCode] <= 10)){
                                return;
                            }
                            break;

                        case 'keyup':
                            element._ul_keyups[e.keyCode] = curtime;
                            setTimeout(()=>{
                                if((e.keyCode in element._ul_keydowns) && (element._ul_keydowns[e.keyCode] >= curtime)){
                                    return;
                                }
                                sendEvent(e, okey, attr_map);
                            }, 10)
                            return;
                    };
                    //if ('vy' in e && !(e.vy >-999 && e.vy<999)){
                    //    console.log(e.target._ul_mousemoves, e._ul_timestamp)
                    //}
                    sendEvent(e, okey, attr_map);
                })
            }
        }

        function setElementObserver(element, attribute_list){
            console.log("unsupport method setElementObserver")
            return ;
        }

        function addChild(element, it){
            let [it_id, it_method, it_args] = it
            let it_type = it_args['html_type'];
            let child = document.createElement(it_type);
            element.appendChild(child);
            child.id = it_id
            for (let key in it_args){
                that.cmd_target(child, key, it_args[key])
            }
        }

        //if (method in target){
            //target[method] = args
        //    target.setAttribute(method, args)
        //}else{
            switch (method){

                case "textContent":  // 用于不兼容textContent的浏览器
                    target.innerText = args;
                    break;

                case "addChild":
                    addChild(target, args)
                    break;

                case "removeChildsById":
                    for (let [left, count] of args){
                        while (count>0 & target.children.length>0){
                            count --;
                            target.removeChild(target.children[left])
                        }
                    }
                    break;

                case "any":
                case "setAttributes":
                    for(let key in args){
                        that.cmd_target(target, key, args[key])
                    }
                    break;

                case "html_type":
                    break;

                case "setEvents":
                    setElementEvents(target, args)
                    break;

                case "setStyles":
                    for (let sname in args){
                        target.style[sname] = args[sname]
                    }
                    break;

                case "scrollBottom":
                    target.scrollTop = target.scrollHeight;
                    break;

                case "setObservers":  // 没什么用， 待废除
                    setElementObserver(target, args)
                    break;

                case "addChilds":
                    for (let it of args){
                        addChild(target, it)
                    }
                    break;

                case "contextmenu":
                    let contextMenuHandler = function contextMenuHandler(e){
                        e.preventDefault();
                        return false;
                    }
                    if (args){
                        target.removeEventListener('contextmenu', contextMenuHandler);
                    }else{
                        target.addEventListener('contextmenu', contextMenuHandler);
                    };
                    break;

                case "onmousedown":
                    target.onmousedown = args
                    break;

                case "lockpointer":
                    // console.log(target, args)
                    if (args){target.requestPointerLock();}else{document.exitPointerLock();};
                    break;

                case 'focus':
                    target.focus();
                    break;

                case 'fullscreen':
                    console.log('fullscreen', target);
                    target.requestFullscreen();
                    break;

                case 'display':
                    if (args != null){
                        target.style.display = args
                    }
                    break;


                default:
                    target[method] = args
                    // console.log('cmd_target default: ', method, args)
                    target.setAttribute(method, args);

            //}
        }



    }

    cmd_loop(){
        /*
         cmd: "{id}.{method_or_attribute}": args
         */
        fetch(this.pcmd)
			.then(response => response.json())
			.then(list_obj=>{
                // console.log(list_obj)
				for (var it of list_obj){
                    let [target_id, method, args] = it
                    switch (target_id){
                        case "system":
                            this.cmd_system(method, args)

                            break;
                        default:
                            if(this.handshaking){
                                break;
                            }
                            let target = null;
                            if (target_id == this.ui_tag){
                                target = document
                            }else{
                                target = document.getElementById(target_id);
                            }
                            this.cmd_target(target, method, args)
                            break;
                    }
				}
				this.err_count = -1
				requestAnimationFrame(this.cmd_loop.bind(this));
			})
			.catch((error) => {
                console.log(error)
                // return; // debug
                if(this.err_count == -1){
                    window.location.href = "about:blank";
                    window.close();
                }
                this.err_count += 1
                if (this.err_count < 10){
                    requestAnimationFrame(this.cmd_loop.bind(this));
                }else{
                    window.location.href = "about:blank";
                    window.close()  // 断开连接后关闭窗口
                }

			})
			.finally(() => {

			});
    }

    test(){
        console.log('test');
        console.log(this.root)
    }
}
