import theano
from theano import tensor as T

a=T.scalar()
b=T.scalar()
y=a*b

multiply = theano.function(inputs=[a, b], outputs=y)

print multiply(3, 4)
print multiply(4, 33)