# the authors names Isa Grace and Ellen Kevin and Camryn Hurley
l={'flour':1.5,'baking powder':2 ,'salt':1/2,'unsalted butter':1/2,'granulated sugar':1,'eggs':2,'pure vanilla extract': 1.5, 'milk':1/2,'zest of lemons':2}
r={'flour': 3,'baking soda':1,'unsweetened natural cocoa powder':2,'salt':1/2,'unsalted butter':1/2,'granulated sugar':2,'canola':1,'eggs':4,'pure vanilla extract':1,'white vinegar':1,'red food coloring':4,'buttermilk':1}
def similar(x,y):
    matches=[]
    for c in l:
            if c in l:
                if c in r:
                    matches.append(c)
                else:
                    None
            else:
                None
    print(matches)

similar(l,r)
