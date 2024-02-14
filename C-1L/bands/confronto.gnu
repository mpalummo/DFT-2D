set xtics ("{/Symbol G }" 0.0000 , "K" 0.6667 , "M" 1.0000 ,"{/Symbol G }" 1.5773)

plot 'LDA/graphene_LDA.dat.gnu' w l lw 2 lc rgb 'red' t 'LDA' , 'PBE/graphene_PBE.dat.gnu' w l lw 2 lc rgb 'blue' t 'PBE'
