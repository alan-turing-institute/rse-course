
<xsl:stylesheet version="2.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="xml" indent="yes" omit-xml-declaration="yes" />
        
    <!-- Decompose reaction into "reactants \rightarrow products" -->
    <xsl:template match="//reaction">
        <xsl:apply-templates select="reactants"/>
        <xsl:text> \rightarrow </xsl:text>
        <xsl:apply-templates select="products"/>
        <xsl:text>\\&#xa;</xsl:text>
    </xsl:template>
        
    <!-- For a molecule anywhere except the first position write " + " and the number of molecules-->
    <xsl:template match="//molecule[position()!=1]">
        <xsl:text> + </xsl:text>
        <xsl:apply-templates select="@stoichiometry"/>
        <xsl:apply-templates/>
    </xsl:template>

    <!-- For a molecule in first position write the number of molecules -->
    <xsl:template match="//molecule[position()=1]">
        <xsl:apply-templates select="@stoichiometry"/>
        <xsl:apply-templates/>
    </xsl:template>

    <!-- If the stoichiometry is one then ignore it -->
    <xsl:template match="@stoichiometry[.='1']"/>
    
    <!-- Otherwise, use the default template for attributes, which is just to copy value -->
    
    <!-- Decompose element into "symbol number" -->
    <xsl:template match="//atom">
        <xsl:value-of select="@symbol"/>
        <xsl:apply-templates select="@number"/>
    </xsl:template>
        
    <!-- If the number of elements/molecules is one then ignore it -->        
    <xsl:template match="@number[.=1]"/>
    
    <!-- ... otherwise replace it with "_ value" -->        
    <xsl:template match="@number[.!=1][10>.]">
        <xsl:text>_</xsl:text>
        <xsl:value-of select="."/>
    </xsl:template>
        
    <!-- If a number is greater than 10 then wrap it in "{}" -->        
    <xsl:template match="@number[.!=1][.>9]">
        <xsl:text>_{</xsl:text>
        <xsl:value-of select="."/>
        <xsl:text>}</xsl:text>          
    </xsl:template>
        
    <!-- Do not copy input whitespace to output -->
    <xsl:template match="text()" />
</xsl:stylesheet>
