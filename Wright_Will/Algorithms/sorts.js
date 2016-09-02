/// MERGE SORT !!!!!!!!!
function merge(a,b){
	var out = [];
	if(a.length>1){
		a = a.reverse()
	}
	if(b.length>1){
		b = b.reverse()
	}
	while (a.length >0 || b.length>0){
		if(a.length === 0){
			out.push(b.pop());
		}else if(b.length === 0){
			out.push(a.pop());
		}else if(a[a.length-1]<b[b.length-1]){
			out.push(a.pop());
		}else{
			out.push(b.pop());
		}
	}
	return out;
}

function mergeSort(arr){
	if(arr.length === 1) {
		return arr;
	}
	var mid = Math.ceil(arr.length/2);
	var a = arr.slice(0,mid);
	var b = arr.slice(mid);
	return merge(mergeSort(a),mergeSort(b));
}

//var arr3 = [3,5,3,7,9,111,2,4,555,0,6,2,5,8,1,3,8,4,3,9,33,55,77,11,0]
//var arr = [0,2,3,7]
//var arr2 = [0,1,3,22]
//var out = mergeSort(arr3)

//console.log(out)

//insertion sort  --------------------------------------------------
function insertSort(arr){
	var out =[];
	while(arr.length > 0){
		let max = arr[0];
		index = 0;
		for(let i = 1;i<arr.length;i++){
			if(arr[i]>max){
				max = arr[i];
				index = i;
			}
		}
		out.push(...arr.splice(index,1));
	}
	return out;
}

//arr = [1,5,0,25,67,1,89,2,90,45,0,2]
//var out = insertSort(arr)
//console.log(out)

//bubble Sort -------------------------------------------------------
function bubbleSort(arr,n){
	n = n || arr.length;
	for(let i =0;i<n;i++){
		arr.forEach(function(x,i,arr){
			if(arr[i]>arr[i+1]){
				var temp = arr[i];
				arr[i] = arr[i+1];
				arr[i+1] = temp;
			}
		})
	}
	return arr;
}

//arr = [1,5,0,25,67,1,89,2,90,45,0,2]
//var out = bubbleSort(arr)
//console.log(out)
