#!/usr/bin/node

exports.esrever = function (list) {
    let len = list.length - 1;
    let newList = [];
    for (let i = len; 0 <= i; i--) {
	newList.push(list[i]);
    }
    return newList;
}

