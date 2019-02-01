
#1.在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
#思路：右上角开始，比输入值小，则j+1，比输入值大，则i-1，len(array)为行数，len(array[0])为列数
# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        if not array:
            return False
        row = len(array)-1
        col= len(array[0])-1
        i = 0
        j = col
        while i<=row and j>=0:
            if target<array[i][j]:
                j -= 1
            elif target>array[i][j]:
                i += 1
            else:
                return True
        return False

		
#2.请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
#思路：replace 函数进行替换即可
# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        s=s.replace(' ','%20')
        return(s)
		
		
#3.输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。
#思路：核心在于::-1倒叙返回，其他只需要遍历获取值即可
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        newlist = []
        if listNode is None:
            return newlist
        while listNode:
            newlist.append(listNode.val)
            listNode=listNode.next
        return (newlist[::-1])
		
		
#4.输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
#思路：
#要点一：最简单的中序遍历就是把图按位置画好从左到右投影下来就对了
#二：前序：根左右，中：左根右，后：左右根
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if len(pre)==0 or len(tin)==0:
            return None
        root_data = pre[0]
        i = tin.index(root_data)
        left = self.reConstructBinaryTree(pre[1:i+1],tin[:i])#pre为何不是[0,i]存疑
        right = self.reConstructBinaryTree(pre[i+1:],tin[i+1:])
        tree = TreeNode(root_data)
        tree.left = left
        tree.right = right
        return tree
		
#5.用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
#思路：两个栈一个用来入队push，再把一个栈的出栈压入第二个栈，再从第二个栈出栈来实现队列出操作，即pop，因为两个栈共同模拟队列，因此任何操作都要注意判断两个栈是否空，可能会出现需要出队列，但是栈1有数据，栈2为空，此时就需要先将栈1的数据取出压入栈2，再进行相应操作
#要点：栈是先入后出，队列是先入先出
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
         
    def push(self, node):
        # write code here
        if len(self.stack1) == 0:
            while len(self.stack2):
                self.stack1.append(self.stack2.pop())
        self.stack1.append(node)
         
    def pop(self):
        # return xx
        if len(self.stack2) != 0:
            return self.stack2.pop()
        else:
            while len(self.stack1):
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
		
		
#6.把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。 输入一个非减排序的数组的一个旋转，输出旋转数组的最小元素。 例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。 NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
#思路：最笨是一个个顺序查找，也可以二分法
#方法1：顺序查找
# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if len(rotateArray)==0 :
            return 0
        if len(rotateArray)==1 :
            return rotateArray[0]
        else :
            c=rotateArray[0]
            for i in range (len(rotateArray)-1):
                b=rotateArray[i+1]
                if b<=c:
                    c=b
                if b>c:
                    c=c
            return c
#改进：不用查找到最后，只要出现前一个大于后一个，返回后一个即可，是非减数列旋转
# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if len(rotateArray)==0 :
            return 0
        if len(rotateArray)==1 :
            return rotateArray[0]
        else :
            for i in range(len(rotateArray)-1):
                if rotateArray[i] > rotateArray[i+1] :
                    return rotateArray[i+1]
            return rotateArray[0]

#方法2：二分法查找
# -*- coding:utf-8 -*-
# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        if len(rotateArray)==0 :
            return 0
        if len(rotateArray)==1:
            return rotateArray[0]
        if len(rotateArray)==2:
            if rotateArray[0]>=rotateArray[1]:
                return rotateArray[1]
            else:
                return rotateArray[0]
        else :
            left=0
            right=len(rotateArray)-1  #序列从0开始，最后的序号比值小1
            while(right-left>1):      #保证中间至少有数
                mid=(left+right)/2
                if rotateArray[left]<=rotateArray[mid]:
                    left=mid
                else: 
                    right=mid         #就算最后剩三个，保证mid指向第一个旋转处，将right取mid返回
            return rotateArray[right]
			
#7.大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。n<=39
#思路：斐波拉契用到了前两个值，最开始几个值直接给出，后面的迭代即可
#方法：迭代/递归
# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n>39:
            return False
        if n==0:
            return 0
        if n==1 or n==2:
            return 1
        count, a, b = n, 1, 1
        while count-2>0:
            a, b = b, a+b
            count -= 1
        return b
		
#8.一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
#思路：写了几项，发现和斐波拉契数列很像，是0，1，2，3，5。。。
#方法：递归/迭代
# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        list=[0,1,2]
        if number<0:
            return False
        if number<=2:
            return list[number]
        else:
            while(len(list)<=number):
                list.append(list[-1]+list[-2])
            return list[number]
			
#9.一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
#思路：寻找f(n)与之前函数的关系
#方法：第一次跳1，后面剩n-1，即f(n-1)...一直到f(2)=2f(1)，f(1)=1,故f(n)=2^(n-1)
# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        # write code here
        if number<=0:
            return False
        if number==1:
            return 1
        else:
            a=1
            for i in range (number):
                a=a*2
            return (a/2)
			
#10.我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
#思路：画图找规律
#方法：类似斐波拉契
# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        if number<=0:
            return False
        if number==1:
            return 1
        if number==2:
            return 2
        count, a, b = number, 1, 2
        for i in range(count-2):
            a, b = b, a+b
        return b
		
#11.输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
#思路：正数二进制为原码，负数得高位补1；正数反码原码相同，负数是原码除符号位全取反；正数补码原码相同，负数为反码+1
#方法：把一个整数减去1之后再和原来的整数做按位与，得到的结果相当于是把整数的二进制表示中最右边的一个1变成0
#定义：python中的定义：右移n位定义为除以pow(2,n)，左移n位定义为乘以pow(2,n)
#要点：python移位特殊性：高位为1，右移高位会不停补1，判断各位时，应用左移
#https://www.cnblogs.com/cotyb/archive/2016/02/11/5186461.html
# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        count = 0
        if n < 0:
            n = n & 0xffffffff   #n在计算机内部以补码存储，利用&fffffff,可转换成二进制形式
        if n == 0:
            return 0
        while n!=0:
            count += 1
            n = (n - 1) & n
        return count
		
#12.给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
#思路：循环，加入一个计数即可，0，+-1单独讨论，正负单独讨论
#方法：或者快速幂，利用二的倍数，分为奇偶讨论，例如2^5,5为101，末尾为1，无法除，正数右移不影响，为10，即2，2^2*2^2*2；若整除例如2^6,110，为11，3，2^3*2^3相乘得出，在讨论正负输出问题
#正常做法
# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        num=exponent
        if exponent==0:
            return 1
        if exponent==1:
            return base
        if exponent==-1:
            return (1/base)
        if exponent>0:
            a=exponent
            b=base
            while(a>1):
                b=base*b
                a-=1
            return b
        if exponent<0:
            a=exponent
            b=base
            while(a<-1):
                b=base*b
                a+=1
            return(1/b)
			
#对于调用自己，使用self.即可，前面使用斐斐波拉契时这么调用出错，原因待查
#快速幂
# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        a=base
        b=abs(exponent)
        if(exponent==0):
            return 1
        if (exponent==1):
            return base
        if (exponent==-1):
            return 1/base
        c=self.Power(base,b>>1) #关键在此，多用移位来进行乘除运算！
        if b&0x1==0:
            c=c*c
        if b&0x1==1:
            c=c*c*base
        if exponent<0:
            c=1/c
        return c

#13.输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
#思路：两个数组，利用取余来判断，再合并；应该可以用两个变量从前往后记录奇数偶数位置，借助第三个变量进行位置交换（插入排序）
#问题：错误的方法因为使用了迭代，在for循环里，i在不停变化，此时是不可以使用迭代的（原因未知）
#错误
    def reOrderArray(self, array):
        # write code here
        odd=[]
        even=[]
        a=[]
        for i in len(array):
            if (array[i])%2==1:
                b=array[i]
                even.append(b)
            if (array[i])%2==0:
                b=array[i]
                odd.append(b)
        a=add.extent(even)
        return a
		
		
#正确：
# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        odd=[]
        even=[]
        c=len(array)
        i=0
        while i<=c-1:
            if (array[i])%2==1:
                even.append(array[i])
            if (array[i])%2==0:
                odd.append(array[i])
            i+=1
        return even+odd
		
		
#14.输入一个链表，输出该链表中倒数第k个结点。
#思路：遍历找到next为空，即为队末，将其一个个丢入新数组，再取倒数第k个即可
#方法：
#问题：要用return None，不可用return False！先append，再等于next，改变指向！这里是返回节点，不是返回节点.val也不是节点.next！
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        a=[]
        if head is None:
            return None
        while head:
            a.append(head)
            head=head.next
        if k>len(a) or k<1:
            return None
        return a[len(a)-k]

		
#15.输入一个链表，反转链表后，输出新链表的表头。
#思路：和上面相同，先弄到一个数列里，再将数列反向，再进行链表重构即可
#方法：
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        a=[]
        if pHead is None:
            return None
        while pHead:
            a.append(pHead)
            pHead=pHead.next
        a=a[::-1]
        for i in range (len(a)):
            b=a[i]
            if i ==len(a)-1:
                b.next=None
            else:
                c=a[i+1]
                b.next=c
        return a[0]
		
		

#16.输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
#思路：
#方法：
#正确解法，用a=ListNode(0创建一个空链表，采用迭代方法)
#笨办法，仿照15，用数组完成俩个链表遍历/排序，再重构，发现超时。。。
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        a=ListNode(0)
        if pHead1 is None:
            return pHead2
        if pHead2 is None:
            return pHead1
        if pHead1 is None and pHead2 is None:
            return None
        if pHead1.val>=pHead2.val:    #已经使用迭代，不要用while循环包含这个ifelse，开始包含出错了
            a=pHead2
            pHead2=pHead2.next
            a.next=self.Merge(pHead1,pHead2)
        else:
            a=pHead1
            pHead1=pHead1.next
            a.next=self.Merge(pHead1,pHead2)
        return a
		
		
#17.输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
#思路：利用迭代，不停向下查找比对，首先找到相同父节点，判断下面是否完全一致，不一样则再在左子树和右子树查找相同父节点，一直到叶子为止
#方法：
#没做出来参考别人的
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        result = False
        if pRoot1 is None or pRoot2 is None:
            return False
        if pRoot2 is not None and pRoot1 is not None:
            if pRoot1.val == pRoot2.val:
                result = self.equal(pRoot1,pRoot2)
            if not result:
                result = self.HasSubtree(pRoot1.left,pRoot2)
            if not result:
                result = self.HasSubtree(pRoot1.right,pRoot2)
        else:
            return False
        return result
    def equal(self,tree1,tree2):
        if tree2 is None:           #两个if不能换位置，2先空了那就对了，如果2没空1空就错误；反过来1空了就错，如果1没空2空了
            return True
        elif tree1 is None:
            return False
        else:
            c=(tree1.val == tree2.val) and (self.equal(tree1.left,tree2.left)) and (self.equal(tree1.right,tree2.right))
            return c
			
			
#18.操作给定的二叉树，将其变换为源二叉树的镜像。
#思路：遍历各个子树，左变右右变左即可
#方法：
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if root:
            c=root.left
            root.left=root.right
            root.right=c
            self.Mirror(root.right)
            self.Mirror(root.left)
            return root
        else:
            return None
			
			
#19.输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，例如，如果输入如下4 X 4矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
#思路：一圈一圈分析，一圈分四个运动，右，下，左，上，用起始坐标来判断是否转弯，起始各包括两个坐标，因此四个变量来完成一次循环，这几个变量也会自我加减，如果最终触碰边界，则跳出结束
#方法:还有一种奇妙方法，每次取matrix[0],矩阵逆时针90度，再取一直循环直到空/另外zip函数可以实现旋转矩阵，很奇妙
# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        a=[]
        lietou=-1
        hangtou=-1
        liewei=len(matrix[0])
        hangwei=len(matrix)
        lie=0
        hang=0
        while True:
            if liewei==lie:
                break
            while lie<liewei:
                a.append(matrix[hang][lie])
                lie+=1
            lie-=1
            hang+=1
            hangtou+=1
            if hangwei==hang:
                break
            while hang<hangwei:
                a.append(matrix[hang][lie])
                hang+=1
            hang-=1
            lie-=1
            liewei-=1
            if lie==lietou:
                break
            while lie>lietou:
                a.append(matrix[hang][lie])
                lie-=1
            lie+=1
            hang-=1
            hangwei-=1
            if hang==hangtou:
                break
            while hang>hangtou:
                a.append(matrix[hang][lie])
                hang-=1
            hang+=1
            lie+=1
            lietou+=1
        return a
		
		
#奇妙运用zip# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        if matrix:
            top_row=list(matrix[0])  					#取第一行
            array=list(zip(*matrix[1:]))				#取matrix第二行开始做新矩阵，再利用zip（*）旋转，a[i][j]变a[j][i],再转为列表，利用list输出
            array.reverse()								#list里为多个一维数组，reverse改变一维数组顺序，即进行行的交换，这样变后，成了一个逆时针90度旋转矩阵
            return top_row+self.printMatrix(array)      #递归输出即可
        else:
            return []									#空则输出空列表
			
			

#20.定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。
#思路：利用辅助栈完成，入栈时，辅助为空则两个栈都push，后面再push，就将辅助栈顶值与输入值比较，若输入小于等于（等于很关键，在pop处有用）
#再压入辅助栈，因此，min只需要输出辅助栈栈顶值即可，即-1处，再pop这出了点问题，后面发现只要正常删除栈顶数据和辅助栈栈顶不等，辅助栈就不用操作，若相等，则删除，若多个相同最小值，第一个删除，因为等于最小值时辅助栈这边也会重复输入，不会出现错误
#方法：
#问题：一上来没看懂push，pop，top，min函数丢这干嘛
#看了才知道这些时候也要完成功能，push入栈，pop返回删除栈顶数据，top返回栈顶数据，min返回栈中最小值
#因为看到了提示用另一个栈来做，所以这么弄了
#注意：要加self.，开始不加arr，brr两个栈死活说没定义
# -*- coding:utf-8 -*-
class Solution:
    arr=[]
    brr=[]
    def push(self, node):
        # write code here
        self.brr.append(node)
        if not self.arr or node <= self.arr[-1] :
            self.arr.append(node)
    def pop(self):
        # write code here
        if self.brr[-1] == self.arr[-1]:
            self.arr.pop()
        return self.brr.pop()
    def top(self):
        # write code here
        return self.brr[-1]
    def min(self):
        # write code here
        return self.arr[-1]
		
		
		
#21.输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。假设压入栈的所有数字均不相等。例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）
#思路：对于pop序列，j-1号元素在push中序号大于j+1在push中序号大于j在push中序号，则不存在该出栈
#方法：
# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        list=[]
        list1=[]
        if len(pushV)!=len(popV):
            return False
        for i in range (len(popV)):				#这段想用for i in range len(popV):
            for k in range (len(pushV)):		#			list.append(pushV.index(popV[i]))
                if popV[i] == pushV[k]:			#一直报错说超出边界，不知道为啥
                    list.append(k)
                else:
                    pass
        j=1
        if len(list)!=len(popV):
            return False
        while len(list)>=3:
            while j+1<len(list):
                if (list[j-1]>list[j+1] and list[j+1]>list[j] ):
                    list1.append(1)
                j+=1
            else:
                break
        if len(list1)==0:
            return True
        else:
            return False
			
#22.从上往下打印出二叉树的每个节点，同层节点从左至右打印。
#思路：这个是广度优先，常规做法通过一个辅助队列完成
#方法：
#考察广度优先（BFS），深度优先（DFS）
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]

    def PrintFromTopToBottom(self, root):
        list=[]
        list1=[]
        # write code here
        if not root:
            return []
        list1.append(root)
        while len(list1):
            a=list1.pop(0)
            list.append(a.val)
            if a.left:
                list1.append(a.left)
            if  a.right:
                list1.append(a.right)
        return list