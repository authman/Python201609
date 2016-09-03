function bubbleSort(arr){
    for (var n = 0; n < arr.length; n++) {
        for (var i = 1; i < arr.length; i++) {
            if (arr[i-1]>arr[i]) {
                temp = arr[i-1]
                arr[i-1] = arr[i]
                arr[i] = temp
            }
        }
    }
    return arr
}

var a = [1,5,8,12,0,4,8]
