
<xsl:stylesheet version="2.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="xml" indent="yes" omit-xml-declaration="yes" />
        
    <xsl:template match="//reaction">
        <xsl:apply-templates select="reactants"/>
        <xsl:text> \rightarrow </xsl:text>
        <xsl:apply-templates select="products"/>
        <xsl:text>\\&#xa;</xsl:text>
    </xsl:template>
        
    <xsl:template match="//molecule[position()!=1]">
        <xsl:text> + </xsl:text>
        <xsl:apply-templates select="@stoichiometry"/>
        <xsl:apply-templates/>
    </xsl:template>
        
    <xsl:template match="@stoichiometry[.='1']"/>
    <!-- do not copy 1-stoichiometries -->
    
    <!-- Otherwise, use the default template for attributes, which is just to copy value -->
        
    <xsl:template match="//molecule[position()=1]">
        <xsl:apply-templates select="@* | *"/> 
    </xsl:template>
    
    <xsl:template match="//element">
        <xsl:value-of select="@symbol"/>
        <xsl:apply-templates select="@number"/>
    </xsl:template>
        
    <xsl:template match="@number[.=1]"/>
    <!-- do not copy 1-numbers -->
    
    <xsl:template match="@number[.!=1][10>.]">
        <xsl:text>_</xsl:text>
        <xsl:value-of select="."/>
    </xsl:template>
        
    <xsl:template match="@number[.!=1][.>9]">
        <xsl:text>_{</xsl:text>
        <xsl:value-of select="."/>
        <xsl:text>}</xsl:text>          
    </xsl:template>
        
    <xsl:template match="text()" />
    <!-- Do not copy input whitespace to output -->
</xsl:stylesheet>
